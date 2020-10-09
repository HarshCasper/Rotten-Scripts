# EC2 Launcher

## Description
Launch AWS EC2 instance on-demand using simple command

## Prerequisites

AWS IAM account

## Usage Example
```
go run --help
Usage of C:\Users\frbimo\AppData\Local\Temp\go-build379111111\b001\exe\main.exe:
      --dry-run            dry-run
      --num-instance int   number of ec2 instances
pflag: help requested
exit status 2
```
## Environment Variable
| KEY                                  | Required                                                                 | Example                                       |
| ------------------------------------------ | --------------------------------------------------------------------------- | --------------------------------------------- |
| `ACCESS_KEY`                         | Yes                                                           | `` |
| `SECRET_KEY`                                |Yes                                                                   | ``                                     |
| `IMAGE_ID`                         | Yes                                                            | ``                                |
| `REGION`                | Yes                                        | `us-east-2`                                       |
| `INSTANCE_TYPE`       | Yes                                       | `t2.micro`                          |
| `SUBNET_ID`                             | No                                                               | ``                                   |
| `INSTANCE_NAME`                             | Yes                                                                | `test-instance`                                        |
| `TAGS`                          | No        (format: "key1,value1;key2,value2")                                               | `type,production`                                       |
| `KEYPAIR`                      | No                                                       | ``                                          |

