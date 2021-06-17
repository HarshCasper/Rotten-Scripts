package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"strings"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/ec2"
	"github.com/spf13/pflag"
	"github.com/spf13/viper"
)

var dryrun bool

func init() {
	var instanceNum int
	flag.IntVar(&instanceNum, "num-instance", 0, "number of ec2 instances")
	flag.BoolVar(&dryrun, "dry-run", false, "dry-run")

	pflag.CommandLine.AddGoFlagSet(flag.CommandLine)
	pflag.Parse()
	viper.BindPFlags(pflag.CommandLine)
}

// Config contains given value from .env file
type Config struct {
	NumInstance  int64
	AccessKey    string
	SecretKey    string
	Region       string
	InstanceName string
	InstanceType string
	ImageID      string
	SubnetID     string
	Tags         string
	KeyPair      string
}

// ReadAndSet reads given config value and set into existing struct
func (cfg *Config) ReadAndSet() error {
	viper.SetConfigName("config")
	viper.SetConfigType("env")
	viper.AddConfigPath("./config")
	err := viper.ReadInConfig()
	if err != nil {
		return fmt.Errorf("Error env file: %s", err.Error())
	}

	cfg.AccessKey = viper.GetString("ACCESS_KEY")
	cfg.SecretKey = viper.GetString("SECRET_KEY")
	cfg.Region = viper.GetString("REGION")
	cfg.InstanceName = viper.GetString("INSTANCE_NAME")
	cfg.InstanceType = viper.GetString("INSTANCE_TYPE")
	cfg.ImageID = viper.GetString("IMAGE_ID")
	cfg.SubnetID = viper.GetString("SUBNET_ID")
	cfg.Tags = viper.GetString("TAGS")
	cfg.KeyPair = viper.GetString("KEYPAIR")

	return nil
}

// SetInstanceNumber sets given number of instance user demanded
func (cfg *Config) SetInstanceNumber(num int64) {
	cfg.NumInstance = num
}

func (cfg *Config) LaunchInstance() (*ec2.Reservation, error) {
	sess, _ := session.NewSession(
		&aws.Config{
			Region:      aws.String(cfg.Region),
			Credentials: credentials.NewStaticCredentials(cfg.AccessKey, cfg.SecretKey, ""),
			// MaxRetries sets to 0 to prevent duplicated instance requests on unreliable network condition
			MaxRetries: aws.Int(0),
		})

	svc := ec2.New(sess)

	opt := &ec2.RunInstancesInput{
		DryRun:       aws.Bool(dryrun),
		ImageId:      aws.String(cfg.ImageID),
		InstanceType: aws.String(cfg.InstanceType),
		MinCount:     aws.Int64(1),
		MaxCount:     aws.Int64(cfg.NumInstance),
	}
	if cfg.SubnetID != "" {
		opt.SubnetId = aws.String(cfg.SubnetID)
	}
	if cfg.KeyPair != "" {
		opt.KeyName = aws.String(cfg.KeyPair)
	}

	runResult, err := svc.RunInstances(opt)
	if err != nil {
		return nil, err
	}

	tags := []*ec2.Tag{}
	for k, v := range parseTags(cfg.Tags) {
		tags = append(tags, &ec2.Tag{
			Key:   aws.String(k),
			Value: aws.String(v),
		})
	}

	if len(tags) > 0 {
		for _, instance := range runResult.Instances {
			_, err = svc.CreateTags(&ec2.CreateTagsInput{
				Resources: []*string{instance.InstanceId},
				Tags:      tags,
			})
			if err != nil {
				return nil, err
			}
		}
	}

	return runResult, nil
}

func prettyJSON(input interface{}) string {
	b, _ := json.MarshalIndent(input, "", " ")
	return string(b)
}

func parseTags(tags string) map[string]string {
	m := map[string]string{}
	for _, tag := range strings.Split(tags, ";") {
		if kv := strings.Split(tag, ","); len(kv) == 2 {
			m[kv[0]] = kv[1]
		}
	}
	return m
}

func main() {
	cfg := &Config{}
	err := cfg.ReadAndSet()
	if err != nil {
		panic(err)
	}

	cfg.SetInstanceNumber(viper.GetInt64("num-instance"))
	output, err := cfg.LaunchInstance()
	if err != nil {
		panic(err)
	}

	fmt.Println()
	fmt.Println(prettyJSON(output))
}
