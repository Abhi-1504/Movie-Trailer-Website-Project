# Movie Trailer : Server side code
The code, when executed takes inputs from users in one of the two ways :
1. **manually**
2. **reading a file**

## Files
The overall `code` has been divided into different **modules** namely:
* input_type_classifier.py
* entertainment_center_input_file_reader.py
* entertainment_center_manual.py
* media.py
* fresh_tomatoes.py

### Sample Input file
`sample_input.txt` - As the name suggests is a sample input file along with other files.
**Users** can define their own customized `input file` for **__reading a file__** method by following the below `pattern`:
```
<--First line should be the no. of movies (integer)-->
<--1st movie name-->
<--1st movie brief description-->
<--1st movie poster image link-->
<--1st movie YouTube trailer link-->
<--2nd movie name-->
<--2nd movie brief description-->
<--2nd movie poster image link-->
<--2nd movie YouTube trailer link-->
.
.
.
<--nth movie name-->
<--nth movie brief description-->
<--nth movie poster image link-->
<--nth movie YouTube trailer link-->
```

## Execution of the Code
The Project has been designed to give menu driven interface to the __user__.
Below are the steps to execute the code:
1. `input_type_classifier.py` file should be executed first*
2. Input M or m for manual entry of values or I or i for reading an input file should be given by the user
3. Based on given entry function from `entertainment_center_manual` __(Manual entry)__ or `entertainment_center_input_file_reader` __(reading from a file)__ is called.
4. HTML page is dynamically generated , **YouTube trailer** can be watched by clicking the poster image of the movie
