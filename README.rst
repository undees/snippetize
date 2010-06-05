Welcome
=======

Snippetize helps you keep the code snippets on your presentation slides up to date.  It's designed to work with Keynote, but could be adapted to any presentation software capable of saving XML (including OpenOffice and PowerPoint).

Install
-------

Do these steps once on your machine:

1. Install the pygments and py-dom-xpath libraries (``sudo`` where appropriate)::

     easy_install pygments

     easy_install py-dom-xpath

2. Set up Keynote to save uncompressed presentations (no ``sudo``)::

     defaults write com.apple.iWork.Keynote SaveCompressionLevel 0

3. Check out Snippetize from http://github.com/undees/snippetize to a directory on your hard drive somewhere.

Prepare
-------

Do these steps once for each new presentation.

1. Prepare the syntax-highlighting sample, which you'll use later to train Keynote. There are a couple of ways to do this, depending on which editor you use:

  * With TextMate:

    i. Open ``styles.rb`` in TextMate.

    ii. Run the "Create HTML From Document" command from the TextMate bundle.  A window should pop up.

    iii. Highlight and copy all the code from the HTML preview window.  You'll paste it into Keynote later.

  * Without TextMate:

    i. Run the following commands::

         pygmentize -f html -O full,style=fruity style.rb > style.html

         open style.html

    ii. Hightlight and copy all the code from your browser window.  You'll paste it into Keynote later.

2. Train Keynote to recognize your syntax colors.

  i. Create an empty slide in your presentation.

  ii. Paste the code you copied previously into it.

  iii. Get the position and font size looking how you want them.

  iv. Bring up the Inspector window for the text box containing your code.

  v. Make the entire box a hyperlink to ``http://localhost/style``.  (You `don't` need to make a web page available at this address; this is just a special URL to help Snippetize find this slide.)

  vi. From the Slide menu, choose "Skip Slide" to make this slide hidden.

3. Generate a config file for Snippetize.

  i. Run ``configurize.py slides.key > config.py``.

  ii. Tweak the ``base`` and ``snippets`` settings inside ``config.py`` based on the instructions in the file.

Write
-----

Do these steps once for each slide that's going to contain code.

1. Create a new, blank slide.

2. Create a new text box on that slide.

3. Give the text box an appropriate position and font size for code.

4. Bring up the Inspector window for the text box.

5. Decide which file and (optionally) part of the file this slide will contain.  For example, you may want to show a snippet named "foo" in a file called ``example.py``.

6. Make the entire box a hyperlink to your file and part, in the following style: ``http://localhost/example.py?foo``.  (You `don't` need to make a web page available at this address; this is just a special URL to help Snippetize find this slide.)

Update
------

Do this step each time you want to update your slides with fresh code::

  snippetize.py slides.key slides_out.key config.py

If you just want to update one snippet, you can name that snippet as a final parameter::

  snippetize.py slides.key slides_out.key config.py example.py\?foo

Consider
--------

This is quite a bit of up-front work; the payoff is less maintenance work as you update your code.  The sweet spot for this is a presentation that has both many code and non-code slides.  If your talk is nearly all code and shell sessions, something like http://github.com/schacon/showoff may be a better fit.
