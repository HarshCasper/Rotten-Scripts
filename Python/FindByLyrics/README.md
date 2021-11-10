# FindByLyrics

Python script to get song lyrics or find a song from a snippet of it's lyrics, and more.

<img style="width: 480px" src="https://ik.imagekit.io/matthewwisdom/findbylyrics_k-IHrKJzK-.jpg?updatedAt=1634993639426" alt="findbylyrics">

## Usage

<pre>usage: main.py [-h] [-e | -t] [-n GENDER] [-a] [-m] [-l] [-g GENRE]
               [-o OUTPUT] [-d DECADE] [-c COUNT] [-y YEAR] [-s STYLE] [-b]
               [--listener] [--full-lyrics] [-p PAGE]
               st

positional arguments:
  st                    The lyric snippet or search term.

optional arguments:
  -h, --help            show this help message and exit
  -e, --exact-match     Only return results with an exact match within them.
  -t, --exact-title     Only return results that have an exact match in the
                        titles.
  -n GENDER, --gender GENDER
                        Genders to match: m for male, f for female, g for
                        groups. Or a comma seperated list of values.
  -a, --artists         Return artists that match can be combined with -l and
                        -m.
  -m, --albums          Return albums that match can be combined with -a and
                        -l
  -l, --lyrics          Return lyrics that match can be combined with -a and
                        -m
  -g GENRE, --genre GENRE
                        Return matches in the genre(s). Genre can be a music
                        genre or a comma seperated list of genres. The
                        genre(s) is matched against the programs list and the
                        best matches are choosen
  -o OUTPUT, --output OUTPUT
                        Output the search results to json file specified in
                        the argument.
  -d DECADE, --decade DECADE
                        Only return results in the specified decade(s) where
                        each decade is represented by the first year in the
                        decade (e.g 1930 for the 30&apos;s).Value can be a value or
                        a comma seperated list of values between the decades
                        1930 and 2020
  -c COUNT, --count COUNT
                        Return count number of matches. Defaults to 1
  -y YEAR, --year YEAR  Only return results from the year(s) specified in the
                        value, The value can be a single year or a comma
                        seperated list of years. Note: Years can only be
                        between 1900 and this year.
  -s STYLE, --style STYLE
                        Specify the style(s). Styles can be gotten from
                        lyrics.com
  -b, --download-full-lyrics
                        Download the full lyrics of all songs matched into
                        individual txt files.
  --listener
  --full-lyrics         Print full lyrics from match.
  -p PAGE, --page PAGE  This program was originally build to scrape the first
                        page of each result but this argument allows you to
                        scrape multiple explicitly specified pages. The value
                        can be a page number, a comma seperated list of page
                        numbers or a range of page numbers in the format a-z
                        where a is the start page and z is the end page.
</pre>
