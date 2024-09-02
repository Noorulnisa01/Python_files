# 1. Headings in Markdown
There is 6 types of headings in markdown.

# Heading 1
- type # and then enter " space " and type your heading text like " Heading 1 ".

## Heading 2
- type ## and then enter " space " and type your heading text like " Heading 2 ".
- Heading 2 can have subheading of Heading 1.

### Heading 3
- type ### and then enter " space " and type your heading text like " Heading 3 "
- Heading 3 can have subheading of Heading 2.
  
#### Heading 4
- type #### and then enter " space " and type your heading text like " Heading 4 ".
- Heading 4 can have subheading of Heading 3.


# 2. Block of Words

This is the normal text.

> This is a blockquote (special text).
>
> when we type > we get a blockquote
>
> we type double time enter to get a new line or text on next line.
>
> you can see the special text that is in the blockquote in the preview window.

# 3. Line break

-- This is a line break

- Line break is done by using double times enter.
- Line bread is created by using the symbol " \ ".
  
# 4. Combine things togethor

## 4.1 Combine two things

Combine two things like block of words and heading

> ## Heading 2

## 4.2. Combine three things

Combine three things like block of words, heading and list

> ## Heading 2
>
> - List item 1
> - List item 2

# 5. Face of text

> ## i) **Bold**

**Bold** - by using double asterisk " ** "

**Bold** - by using double underscore " __ "

> ## ii) *Italic*

*Italic* - by using single asterisk " * "

*Italic* - by using single underscore " _ "

> ## iii) ~~Strikethrough~~

~~Strikethrough~~ - by using double tilde " ~~ "

> ## iv) Superscript

superscript - by using the symbol " ^ "
e.g. 2^3 = 8

> ## v) Subscript

subscript - by using the symbol " ~ "
e.g. 2~3 = 1/2

# 6. Bullet list

> we can use three symbols for bullet lists:
>
> - by using " - "
> - by using " * "
> - by using " + "

- List item 1
- List item 2
- List item 3
  - List item a
  - List item b
    - List item 1
- List item 4
  
> if we create ***bullet for sublist of list***
>
> - we use one time **tab** key and then  **-  /  *  /   +**.
>
> if we create ***bullet for sublist of sublist***
>
> - we use two time **tab** key and then **- / * / +**.

# 7. Number list

1. List item 1
2. List item 2
3. List item 3
    1. List item a
    2. List item b
    1. List item 1
4. List item 4

# 8. Line break / Page break

> we can you three symbol to create line break / page break:
>
- by using three underscore   " _ "

___

- by using three hyphen   " - "

---

- by using three astrick " * "

***

# 9. Link and Hyperlink

> a) Direct Links and Hyperlinks

- we can paste direct link or hyperlink by using **" <> "** symbol.
- For example: <http://www.google.com>
  
        <http://www.google.com>

> b) Text/channel name as a link

- Write the text/words in Square brackets [] and then paste hyperlink by using **" () "** symbol.
- For example: [Google link](http://www.google.com)
  
        [Google link](http://www.google.com)

> c) Key of link

1. Write the text/words in **Square brackets** [ ] , type **semicolon** **" : "** then paste hyperlink .
   - For example: [Youtube]:<http://www.youtube.com>
  
            [Youtube]: http://www.youtube.com
2. Write the word in square bracket [ ] and then type the key of the link.
   - For example:
  
            To open the Youtube link click [here][Youtube].

3. Join the point 1. and 2.

            [Youtube]: http://www.youtube.com
            To open the Youtube link click [here][Youtube]

   This type of link is called key of link.

   [Youtube]: http://www.youtube.com
    To open the Youtube link click [here][Youtube]

# 10. Image and figure with links

Same like link of channels and hyperlinks.

To insert image in markdown 
 
 > ## 10.1 Method # 1: Make the text as hyperlink of image.
  - Dwonload the image in your computer
  - Type the image name in [ ].
  - paste the image link in ( ).
For example: 

[Goggle](https://th.bing.com/th/id/R.4ea7270debc77a8076d7311678d0bc03?rik=%2bCxfbiSpkhxfpg&pid=ImgRaw&r=0)

> ## 10.2 Method # 2: Insert online image in markdown

Same like methode # 1 with add symbol of " ! " before the image name.


![Goggle](https://th.bing.com/th/id/R.4ea7270debc77a8076d7311678d0bc03?rik=%2bCxfbiSpkhxfpg&pid=ImgRaw&r=0)

# 11. Adding Table in Markdown

- we can creat table in markdown by using **" | " **.
- This symbol " | " is called pipe symbol.
- We cab separate the column in table by using **" | " **.

> ## Steps to create tables:
>
 1. Create a table by using pipe symbol.
2. Separate the each ***Cloumn name*** by using pipe symbol.
3. Write the first column name and type " | " and then write the second column name and type " | " and so on.
4. In the second row type dash symbol " ---- " instead of column name.
5. In the third row type the data of each column and separate by using pipe symbol.
6. so on.


For example:

    | Roll no. | Name     | Age | Marks|
    | -------- | -------- | ----| ---- |
    | 1  | Taha     | 21    | 80    |
    | 2  | Bilal     | 22    | 90    |
    | 3  | waleed     | 25    | 60    |
    | 4  | Naseer     | 20    | 84    |

  - It is not necessary that pipe sysmbol to have same width of column but has same no. of column.


> ## Result: 

 | Roll no. | Name     | Age | Marks|
 | -------- | -------- | ----| ---- |
 |  1  | Taha     | 21    | 80    |
 | 2  | Bilal     | 22    | 90    |
 | 3  | waleed     | 25    | 60    |
 | 4  | Naseer     | 20    | 84    |

# 12. Alignment in tables

We can use **" : " ** to align the text in table.

> ## 12.1 left Alignment
  - Wirte " : " on the left side of second row on each cloumn before dashes symbol " ---- "

| Roll no. | Name     | Age | Marks|
| :-------- | :-------- | :----| :---- |
|  1  | Taha     | 21    | 80    |
|  2  | Bilal     | 22    | 90    |
|  3  | waleed     | 25    | 60    |
|  4  | Naseer     | 20    | 84    |

> ## 12.2 Right Alignment

- Write " : " on the right side of second row on each cloumn before dashes symbol " ---- "

| Roll no. | Name     | Age | Marks|
| --------: | --------: | ----:| ----: |
|  1  | Taha     | 21    | 80    |
|  2  | Bilal     | 22    | 90    |
|  3  | waleed     | 25    | 60    |
|  4  | Naseer     | 20    | 84    |

> ## 12.3 Center Alignment

- Write " : " on the both side of  dashes symbol " ---- " of second row on each cloumn.

| Roll no. | Name     | Age | Marks|
| :--------: | :--------: | :----:| :----: |
|  1  | Taha     | 21    | 80    |
|  2  | Bilal     | 22    | 90    |
|  3  | waleed     | 25    | 60    |
|  4  | Naseer     | 20    | 84    |


# 13. Code / Block of Code

- We create a block of code by using **" ``` " **.

- This symbol " ``` " is called code backtick.

For example:

      ```
      x = 10
      y = 20
      z = x + y
      print(z)
      ```
Result:

```
x = 10
y = 20
z = x + y
print(z)
```

- We can also add code by using double time press tab key.
  

# 14. Table of Contents

[1- Headings](#1-headings-in-markdown)\
[2- Block of words](#2-block-of-words)\
[3-Line Break](#3-line-break)\
[4-Combine Things Together](#4-combine-things-togethor)\
[5-Face of text](#5-face-of-text)\
[6-Bullet list](#6-bullet-list)\
[7-Number list](#7-number-list)\
[8-Line break & Page break](#8-line-break--page-break)\
[9-Link and Hyperlink](#9-link-and-hyperlink)\
[10-Image and figure with links](#10-image-and-figure-with-links)\
[11-Adding table](#11-adding-table-in-markdown)\
[12-Alignment in tables](#12-alignment-in-tables)\
[13-Code / Block of Code](#13-code--block-of-code)

