# mre_form_with_imagefields
MRE for StackOverflow

Steps to reproduce error : 

1) Go to http://127.0.0.1:8000/new
2) Fill the form by providing a title and a first image in `file_field` 
3) hit save
4) Go to http://127.0.0.1:8000/edit/1, you should see your form with pre-filled information from previous submission
5) Add a second image in `second_file_field`

You should get validation error, stating that if you provide a title, you should also provide an image.
I would like the files to persist, as they are present at load, I don't see why they aren't part of the POST. 
