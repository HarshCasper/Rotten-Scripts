# File Metadata Extractor

A comprehensive Python script that extracts metadata from various file types including images, audio files, videos, and documents. This tool is perfect for digital asset management, forensic analysis, and file organization.

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## Supported File Types

### Images
- **JPEG/JPG** - EXIF data, dimensions, camera settings
- **PNG** - Dimensions, transparency info
- **TIFF** - EXIF data, multi-page support
- **BMP, GIF** - Basic image properties

### Audio Files
- **MP3** - ID3 tags, bitrate, duration, artist, album
- **FLAC** - Lossless audio metadata
- **WAV** - Audio properties, duration
- **M4A, AAC, OGG, WMA** - Various audio metadata

### Video Files  
- **MP4, AVI, MKV** - Duration, bitrate, basic properties
- **MOV, WMV, FLV, WebM** - Video metadata extraction

### Documents
- **PDF** - Page count, author, creation date, encryption status
- **DOCX** - Author, word count, creation/modification dates

## Features

- **Single File Analysis** - Extract metadata from individual files
- **Batch Processing** - Process entire directories recursively
- **Multiple Output Formats** - JSON and CSV export options
- **Comprehensive Metadata** - File system info + format-specific data
- **Error Handling** - Graceful handling of unsupported files
- **Cross-platform** - Works on Windows, macOS, and Linux

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. **Clone or download** the script to your local machine

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install Pillow mutagen PyPDF2 python-docx
   ```

3. **Make the script executable** (Linux/macOS):
   ```bash
   chmod +x file_metadata_extractor.py
   ```

## Usage

### Basic Usage

**Extract metadata from a single file:**
```bash
python file_metadata_extractor.py /path/to/your/file.jpg
```

**Process all files in a directory:**
```bash
python file_metadata_extractor.py /path/to/directory/
```

**Process directory recursively (including subdirectories):**
```bash
python file_metadata_extractor.py /path/to/directory/ --recursive
```

### Advanced Usage

**Save results to JSON file:**
```bash
python file_metadata_extractor.py /path/to/files/ -o results.json -f json
```

**Save results to CSV file:**
```bash
python file_metadata_extractor.py /path/to/files/ -o results.csv -f csv
```

**Process directory recursively and save results:**
```bash
python file_metadata_extractor.py /path/to/files/ -r -o metadata_report.json
```

### Command Line Options

- `path` - File or directory path to analyze (required)
- `-o, --output` - Output file path (optional)
- `-f, --format` - Output format: json or csv (default: json)
- `-r, --recursive` - Process directories recursively
- `-h, --help` - Show help message

## Output Examples

### Image Metadata (JPEG)
```json
{
  "filename": "photo.jpg",
  "file_size_mb": 2.34,
  "width": 1920,
  "height": 1080,
  "format": "JPEG",
  "exif": {
    "DateTime": "2023:10:15 14:30:22",
    "Camera": "Canon EOS 5D",
    "FNumber": "f/2.8",
    "ISO": "400"
  }
}
```

### Audio Metadata (MP3)
```json
{
  "filename": "song.mp3",
  "file_size_mb": 4.56,
  "duration_formatted": "3:42",
  "bitrate": 320,
  "title": "Amazing Song",
  "artist": "Great Artist",
  "album": "Best Album",
  "year": "2023"
}
```

### PDF Metadata
```json
{
  "filename": "document.pdf",
  "file_size_mb": 1.23,
  "page_count": 15,
  "title": "Important Document",
  "author": "John Doe",
  "creation_date": "2023-10-15T10:30:00"
}
```

## Detailed Explanation

### Metadata Types Extracted

**File System Information (All Files):**
- File name and full path
- File size (bytes and MB)
- Creation, modification, and access timestamps
- File extension

**Image-Specific Metadata:**
- Dimensions (width/height)
- Color mode and format
- EXIF data (camera settings, GPS, timestamps)
- Transparency information

**Audio-Specific Metadata:**
- Duration and bitrate
- Sample rate and channels
- ID3 tags (title, artist, album, year, genre)
- Track numbers and album artist

**Document-Specific Metadata:**
- Page/word counts
- Author and title information
- Creation and modification dates
- Document properties and keywords

### Error Handling
The script gracefully handles:
- Missing or corrupted files
- Unsupported file formats
- Missing dependencies (with helpful error messages)
- Permission errors
- Large file processing

### Performance Notes
- Large directories are processed file by file to conserve memory
- EXIF data from images can be extensive
- Video metadata extraction is limited to basic properties
- PDF processing may be slower for large documents

## Dependencies

- **Pillow (PIL)** - Image metadata and EXIF extraction
- **mutagen** - Audio and video metadata extraction  
- **PyPDF2** - PDF document metadata
- **python-docx** - Microsoft Word document metadata

All dependencies are optional - the script will skip unsupported formats if libraries are missing.

## Author(s)

Created for the Rotten-Scripts repository

## Use Cases

- **Digital Asset Management** - Organize photo/music libraries
- **Forensic Analysis** - Extract file creation timestamps and metadata
- **Content Audit** - Analyze document properties in bulk
- **Data Migration** - Catalog files before/after transfers
- **Media Organization** - Sort files by metadata properties

## Limitations

- Video metadata extraction is basic (duration, bitrate only)
- Some proprietary formats may not be fully supported
- Very large files may take time to process
- DOCX support limited to basic properties
- Requires appropriate permissions to read files

## Future Enhancements

- Support for more video codecs and detailed metadata
- Excel file metadata extraction
- Database output options
- GUI interface
- Batch file renaming based on metadata