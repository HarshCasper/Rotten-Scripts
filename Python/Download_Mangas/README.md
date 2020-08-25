### Download Mangas as PDF

##### Steps

- Libraries/ Modules needed:
  - webdriver-manager
    ```
    pip install webdriver-manager
    ```
  - bs4
    ```
    pip install bs4
    ```
  - selenium
    `pip install selenium`
    &nbsp;
- Using the script
  1. To download a single chapter

     ```
     python download_mangas.py --name <mangaName> --chapter <chapterNumber>
     ```

     Eg:

     ```
     python download_mangas.py --name "One Piece" --chapter 3
     ```

     **Note:** Remember to use double quotes for the manga name

  2. To download all chapter in a given range

     ```
     python download_mangas.py --name <mangaName> --start <startingChapter> --end <endingChapter>
     ```

     **Note:** If you give a number that exceeds the actual ending chapter, then it will download all the available chapters (till the latest chapter) from the mentioned starting chapter.

  3. To download only the first chapter
     ```
     python download_mangas.py --name <mangaName>
     ```
