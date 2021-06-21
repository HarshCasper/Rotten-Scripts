use std::error::Error;
// for downlading the data from youtube
use rustube::{block, Id, VideoFetcher};

mod cli;

fn main() {
    let args = cli::parse_args().expect("Couldn't parse arguments");
    run(args).expect("Failed to download video");
}

// this fucntion handles all the program logic
fn run(args: cli::AppArgs) -> Result<(), Box<dyn Error>> {
    let id = Id::from_raw(&args.url)?;

    // block!() macro is provided by rustube library to run async functions synchronously
    let descrambler = block!(VideoFetcher::from_id(id.into_owned())?.fetch())?;
    println!();
    println!("Downloading '{}'", descrambler.video_title());

    let video = descrambler.descramble()?;

    let to_download = if args.audio_only {
        video.best_audio()
    } else if args.video_only {
        video.best_video()
    } else {
        video.best_quality()
    }
    .unwrap();

    let path = block!(to_download.download())?;
    println!("Downloaded to {}", path.to_str().unwrap_or_default());

    Ok(())
}
