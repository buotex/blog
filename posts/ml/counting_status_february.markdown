{
  "title": "Counting status February",
  "date": "2014-03-03",
  "categories": [
    "counting"
  ],
  "report": [
    
  ]
}



##Experiments

###Ex1

Idea by Uli:
Try old approach, but instead of using the previous dot annotations, we use another approach to
handle elongated cells.

- Draw line, like in pixel classification
- Divide line (when drawing) by the length of the line (measure that somehow)
- We can then continue with gaussian smoothing etc.


Relevant files:

- volumina/brushingcontroler.py
- applets/counting/countingGuiDotsInterface.py

Relevant classes:

- BrushingControler

Behaviour:

On click (not on depress), writeIntoSink is used to write the relevant object into the label-thingy

Checklist:

-[+] First, allow the user to provide multiple labels - let him drag a line instead of just a point

Two possible approaches to provide elongated labels:

1. Write the changed labels directly into the labels-volume, which is difficult as it's uint8
This is partly doable if we scale up to 255... Issue: color table for the labels is then still
broken


2. Do connected components on the label image, divide by size and then put it into training

####Results:

Approach 2 was implemented, working decently well.
Scaling of the colors is ... off, but not easy to change with the current approach, as we have to
calculate stuff manually - the previewlayer does have incorrect values as the scaling isn't done
there
For prediction, it works decently well, as can also be seen from the tetris blocks.


###Ex2
![]({{urls.media}}/counting/results/february/tetrislabels.png)
Now: elongated labels
Working well to differentiate the "blue" tetris blocks from the differently colored ones - 
So more complicated shapes can be dealt with and mapped to 1 per object
![]({{urls.media}}/counting/results/february/tetrisprediction.png)

![]({{urls.media}}/counting/results/february/tetrisproblem.png)
Problem: How do we actually differentiate 4-block and 2-block blocks? We don't manage to do it with
our current pixel-based approach, as not enough context is available.


##Notes ilastik meeting 
{{#todo_block}}
-[+] Instructions for CPLEX, link to tracking page for cplex
Check http://ilastik.github.io/installation/installation.html

Exampledata, Exampleprojects for counting
-[+] Ask Lempitsky/Zisserman if we can mirror their data
Check http://ilastik.github.io/download.html

##Notes: tofix:

-[+]Add tooltip when box is highlighted
-\u2611Perhaps: change cursor to hand when dragging
-[+] Make "live prediction" stretch
-[+]small tool buttons change look -> left side

##Notes: experimenting

- Don't work with keyPressEvent, it's horrible for the boxes as they don't have focus most of the
 time
- self.editor has the current tool status


editor->  BoxController->CoupledRectangleElement-> QGraphicsResizableRect->ResizeHandle

####Change addfiledialogue:
DataSelectionGui->DatasetDetailedInfoTableView->AddButtonDelegate->AddFileButton

Overall: 4 calls to addFileButton
2 * summary
2 * qwidget as parent

Problem: summary can't be changed easily

-change summary
change batch


order: 
1. summary -> addButton
2. detail -> addButton
3. dataSelectionGui.init -> 
4. addButton
5. addButton
6. dataSelectionGui.init

Done

### Gui issues

Note: things that should be in a gui thread should be wrapped into a function which is marked by
@pyqtSlot, otherwise things will break, a lot.

OOOk, setting the font size automatically does not break things, but doing it via the gui does
...wtf?



#More debugging:

2 crashes (till now):

1. an object is its own parent (this->d_ptr->parent == this)
2. item has no valid d_ptr
3. WTF: rectangles are created only when hovering over the rectangle!?



{{/todo_block}}


#Ex3

Now we have to show that our method does decently on the bayer data, as the resolution is much
different.
Hopefully, we still have all the training data used, otherwise we're in trouble.


- Make labelimages for gerlich data
- Label connected components gotten via thresholding
- Calculate distance transform of connected components
- Skeletonize distance transform
- Use skeleton-image as base for labels by applying gaussian filter to the data.



skeleton1, skeleton2: only gaussian magnitude for features
skeleton3: multiple features

dots1: multiple features




#Footnotes
Previous [Report](/posts/ml/counting_status_january) (January 2014)
