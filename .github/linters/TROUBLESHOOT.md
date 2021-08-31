# Troubleshoot

Hello fellow contributors and Open-Source enthusiasts. Welcome to **Rotten-Scripts** :octocat:

This Styling & Troubleshooting guide wil help you to get rid of errors and warnings that might have popped up during the
mandatory **GitHub Checks**.

A list of currently working GitHub Checks can be found [here](../workflows).

In terms of style checking we have these actions -

1. md_lint
2. md_spell
3. md_link
4. py_lint
5. Deepsource

We also have our own separate [STYLING GUIDELINES](../../README.md) as well, you are kindly requested to go through
that file in order to solve all the CODE related errors.

Please be advised that we may even reject a Working Pull Request, if it fails the minimum
`Programming Styles and Standarads`.

In this Troubleshoot guide, we will help you to sort out all the errors related to.

- **Lint Code Base** i.e. [md_lint](../workflows/md_lint.yml)
- **Check Spellings** i.e. [md_spell](../workflows/md_spell.yml)
- **Check Markdown** links i.e. [md_link](../workflows/md_link.yml)

## Lint Code Base

All the Possible Error Codes are mentioned down below. Match your error-code and click on the Link.

This will take you to [markdownlint](https://github.com/DavidAnson/markdownlint).
The rules of styling and possible errors have been taken from this Repository only.

- **[MD001](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md001)** *heading-increment/header-increment* - Heading levels should only increment by one level at a time
- **[MD003](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md003)** *heading-style/header-style* - Heading style
- **[MD004](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md004)** *ul-style* - Unordered list style
- **[MD005](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md005)** *list-indent* - Inconsistent indentation for list items at the same level
- **[MD007](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md007)** *ul-indent* - Unordered list indentation
- **[MD009](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md009)** *no-trailing-spaces* - Trailing spaces
- **[MD010](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md010)** *no-hard-tabs* - Hard tabs
- **[MD011](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md011)** *no-reversed-links* - Reversed link syntax
- **[MD012](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md012)** *no-multiple-blanks* - Multiple consecutive blank lines
- **[MD014](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md014)** *commands-show-output* - Dollar signs used before commands without showing output
- **[MD018](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md018)** *no-missing-space-atx* - No space after hash on atx style heading
- **[MD019](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md019)** *no-multiple-space-atx* - Multiple spaces after hash on atx style heading
- **[MD020](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md020)** *no-missing-space-closed-atx* - No space inside hashes on closed atx style heading
- **[MD021](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md021)** *no-multiple-space-closed-atx* - Multiple spaces inside hashes on closed atx style heading
- **[MD022](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md022)** *blanks-around-headings/blanks-around-headers* - Headings should be surrounded by blank lines
- **[MD023](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md023)** *heading-start-left/header-start-left* - Headings must start at the beginning of the line
- **[MD024](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md024)** *no-duplicate-heading/no-duplicate-header* - Multiple headings with the same content
- **[MD025](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md025)** *single-title/single-h1* - Multiple top level headings in the same file
- **[MD026](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md026)** *no-trailing-punctuation* - Trailing punctuation in heading
- **[MD027](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md027)** *no-multiple-space-blockquote* - Multiple spaces after blockquote symbol
- **[MD028](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md028)** *no-blanks-blockquote* - Blank line inside blockquote
- **[MD029](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md029)** *ol-prefix* - Ordered list item prefix
- **[MD030](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md030)** *list-marker-space* - Spaces after list markers
- **[MD031](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md031)** *blanks-around-fences* - Fenced code blocks should be surrounded by blank lines
- **[MD032](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md032)** *blanks-around-lists* - Lists should be surrounded by blank lines
- **[MD034](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md034)** *no-bare-urls* - Bare URL used
- **[MD036](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md036)** *no-emphasis-as-heading/no-emphasis-as-header* - Emphasis used instead of a heading
- **[MD037](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md037)** *no-space-in-emphasis* - Spaces inside emphasis markers
- **[MD038](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md038)** *no-space-in-code* - Spaces inside code span elements
- **[MD039](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md039)** *no-space-in-links* - Spaces inside link text
- **[MD040](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md040)** *fenced-code-language* - Fenced code blocks should have a language specified
- **[MD041](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md041)** *first-line-heading/first-line-h1* - First line in file should be a top level heading
- **[MD042](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md042)** *no-empty-links* - No empty links
- **[MD043](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md043)** *required-headings/required-headers* - Required heading structure
- **[MD044](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md044)** *proper-names* - Proper names should have the correct capitalization
- **[MD045](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md045)** *no-alt-text* - Images should have alternate text (alt text)
- **[MD046](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md046)** *code-block-style* - Code block style
- **[MD047](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md047)** *single-trailing-newline* - Files should end with a single newline character
- **[MD048](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md048)** *code-fence-style* - Code fence style

## Check Markdown links

This action checks for dead links/broken links.

Kindly ensure that all the links are working before you finalize your Pull Request. A list of possible status code,
and the workaround can be found below.

- 200: Active code - Your link is working properly :grinning:
- 206: Partial success - Only a part of request is being successful, None the less, link is active :grinning:
- 400: Bad Request - A client side error, is there any typographical mistake, Recheck your README, try visiting the
site from your browser too! :thinking:
- 404: Not Found - The website is not responding, is it dead, recheck your README asap, correct the link or add an
alternative. :raised_eyebrow:
- 429: Too many requests - Overwhelming! Just surpassed the rate limit of the website, it's fine, the site is up and
running. :dizzy_face:
- 999: Blocked by agent - Everything is working fine, some agent like LinkedIN and Spotify block multiple request
from their side. It is recommended that you mention this in your PR, so that maintainers can affectively deal
with the error. :roll_eyes:

Don't worry maintainers are trying their best to keep the repository fully automated with minimal errors,
in case you find something you are more than welcome to mention it in your
[Pull Request](https://github.com/HarshCasper/Rotten-Scripts/pulls), open an
[Issue](https://github.com/HarshCasper/Rotten-Scripts/issues), or start a
[Discussion](https://github.com/HarshCasper/Rotten-Scripts/discussions).

**To know more about the _GitHub Actions_, consider checking _[Styling Guidelines](../../STYLE_GUIDELINES.md)_.**
