# Chess-Flowchart

This project is intended to help you create simple looking flowcharts that can help you learn chess openings. You can obviously use the code presented here to generate even more flowcharts, but some openings already have some dedicated files.

## How to use

To generate a flowchart, simply run the following command in the `openings` folder:

`python3 <opening>.py <filename>`

This will generate a file named `filename` with a valid dot format. You can then generate a PNG file using `dot` or copy-paste the content of the file on a website like [Graphviz Online](https://dreampuf.github.io/GraphvizOnline/).

## Creating new openings (and other things)

If you want to generate custom flowcharts, you will have to create your own .py file, in this file then you can create a list of branches that will represent your flowchart. Please find more explanations in the documentation or in [StringReader.py](src/StringReader.py). If you have questions regarding the syntax, please refer to already existing files or raise an issue. Also, note that so far, the model might be incomplete, feel free to add what's missing according to you.

Once your opening is generated, just follow the steps in any pre-existing opening file to generate your flowchart.

## Any problem?

This project is new and therefore a lot of bugs can exist, please raise an issue if you encounter one that you don't understand!