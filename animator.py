import maya.cmds as cmds
import random

def animate(
    number_of_frame,
    step_of_frame,
    translate_min,
    translate_max,
    rotate_min,
    rotate_max,
    scale_min,
    scale_max,
    axes):

    #open the ctrl+z chunk
    cmds.undoInfo(openChunk=True)

    try: 
        #create a list with the selected object
        object_to_animate = cmds.ls(selection=True)

        #for all object ine the object to animate liste
        for obj in object_to_animate:
            #for all frame from 0 to the number of frame
            for frame in range (0, number_of_frame, step_of_frame):
                #for all axe in axes
                for i, axe in enumerate (axes):

                    #create the random value
                    valeur_translate = random.uniform(translate_min[i], translate_max[i])
                    valeur_rotation = random.uniform(rotate_min[i], rotate_max[i])
                    valeur_scale = random.uniform(scale_min[i], scale_max[i])
                    #set the keyframe one the obect
                    cmds.setKeyframe(obj, attribute="translate" + axe, time=frame, value=valeur_translate)
                    cmds.setKeyframe(obj, attribute="rotate" + axe, time=frame, value=valeur_rotation)
                    cmds.setKeyframe(obj, attribute="scale" + axe, time=frame, value=valeur_scale)

            #for the seemless loop
            #for each attribute
            for parametre in ["translate", "rotate", "scale"]:
                #for each axes
                for axe in axes:
                    #save the value at time 0 and put it on each attribute at the end of the loop
                    local_attribute = parametre + axe
                    valeur_de_depart = cmds.getAttr(obj + "." + local_attribute, time=0)
                    cmds.setKeyframe(obj, attribute=local_attribute, time=number_of_frame, value=valeur_de_depart)

    #close the ctrl+z chunk
    finally:
        cmds.undoInfo(closeChunk=True)
