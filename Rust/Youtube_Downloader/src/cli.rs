// for commandline argument parsing
use pico_args::Arguments;

const HELP: &str = "\

ytdl
Download youtube videos from the commandline. Downloads to
current directory by default.

USAGE:
    ytdl [OPTIONS] <URL>

FLAGS:
    -h, --help            Prints help information
    --audio-only          Download audio only
    --video-only          Download video only

ARGS:
    <URL>                 URL of the video to download
";

#[derive(Debug)]
pub struct AppArgs {
    pub url: String,
    pub audio_only: bool,
    pub video_only: bool,
}

pub fn parse_args() -> Result<AppArgs, Box<dyn std::error::Error>> {
    let mut cmdargs = Arguments::from_env();

    // Help has a higher priority and should be handled separately.
    if cmdargs.contains(["-h", "--help"]) {
        print!("{}", HELP);
        std::process::exit(0);
    }

    let args = AppArgs {
        url: cmdargs.free_from_str()?,
        audio_only: cmdargs.contains("--audio-only"),
        video_only: cmdargs.contains("--video-only"),
    };

    // extraneous additional argumetns
    let remaining = cmdargs.finish();
    if !remaining.is_empty() {
        return Err("Additional arguments specifed".into());
    }

    Ok(args)
}
