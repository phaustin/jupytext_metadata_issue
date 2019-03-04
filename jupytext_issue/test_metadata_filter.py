from nbformat.v4.nbbase import new_code_cell, new_markdown_cell, new_notebook
import nbformat
import jupytext.jupytext as jp

toc_meta={"toc": {
   "base_numbering": 1}}

jupytext_meta={"jupytext": {
   "cell_metadata_filter": "all",
   "formats": "ipynb,python//py:percent",
   "notebook_metadata_filter": "all",
   "text_representation": {
   "extension": ".py",
   "format_name": "percent",
   "format_version": "1.2",
   "jupytext_version": "1.0.0"}}}

nb_source = new_notebook()
nb_source['metadata'].update(toc_meta)
nb_source['metadata'].update(jupytext_meta)
new_cell=new_markdown_cell(source="answer here")
new_cell['metadata']={'ques_num':1}
nb_source.cells.insert(0,new_cell)

out_nb=nbformat.writes(nb_source, version=nbformat.NO_CONVERT)
out_jp=jp.writes(nb_source,"py",nbformat.NO_CONVERT)

print(out_nb)
print(out_jp)
assert(out_nb.find('base_numbering') > -1)
assert(out_jp.find('base_numbering') > -1)

