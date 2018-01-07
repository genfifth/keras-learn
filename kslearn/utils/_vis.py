import os
import ipywidgets as widgets
from ipywidgets import Layout, interactive, HBox, VBox
from IPython.display import display

def display_log(path, tb_display_url, cr_model_id=None):
    """
    Display kslearn's model log on jupyter.

    # Arguments
    path: str
        kslearn's model log dir.
    tb_display_url: str
        tensorboard's url.
    cr_model_id: str or None, default=None.
        Default displayed model's id in SimpleGraphPlot.
        When cr_model_id is None, first model which is found by os.listdir is displayed.
        
    # Note
    The port included in the path may be different from tensorboard's listen port.
    So, didn't extract port number from this url and run tensorboard.
    """
    model_ids = []
    for l in os.listdir(path):  
        if os.path.isdir(os.path.join(path, l)):
            model_ids.append(l)
    model_ids.sort()
    
    # Make widget for SimpleGraphPlot
    if cr_model_id is None:
        cr_model_id = model_ids[0]
    image = open(os.path.join(path, cr_model_id, cr_model_id+".png"), "rb")
    image = image.read()
    img_wg = widgets.Image(value=image)

    def f(x):
        image = open(os.path.join(path, x, x+".png"), "rb")
        image = image.read()
        img_wg.value = image

    select_wg = widgets.Select(options=model_ids, value=cr_model_id, description="Model:", disabled=False, 
                               layout=Layout(align_items="flex-start", margin="0px 10px 0px 0px"))
    
    sgp_title_wg = widgets.HTML('<div style="font-family:segoe ui, sans-serif; font-style:italic; font-size:x-large; border-bottom:solid 2.5px #7f7f7f; color:#1987E5; padding-bottom: 3px;">SimpleGraphPlot</div>', 
                                layout=Layout(align_items="flex-start", margin="0px 0px 10px 0px"))
    sgp_contents_wg = HBox([interactive(f, x=select_wg), img_wg], layout=Layout(align_items="flex-start"))
    sgp_wg = VBox([sgp_title_wg, sgp_contents_wg], layout=Layout(height="1080px"))
    
    # Make tab widget
    tab_contents = ["TensorBoard", "SimpleGraphPlot"]
    children = [widgets.HTML("<iframe src=TENSORBOARD_DISPLAY_URL width=100% height=1080px></iframe>".replace("TENSORBOARD_DISPLAY_URL", tb_display_url)),
                sgp_wg, 
               ]
    tab = widgets.Tab()
    tab.children = children
    for i in range(len(children)):
        tab.set_title(i, tab_contents[i])
    display(tab)