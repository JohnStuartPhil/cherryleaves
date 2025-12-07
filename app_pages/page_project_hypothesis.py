import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Business Requirement 1: Hypothesis and Validation")

    st.info(
        f"**Hypothesis** \n"
        f"* We are already aware that there is a visable difference \n"
        f"between a healthy cherry leaf and a cherry leaf with a powdery \n"
        f"mildew on it by looking at an image. \n\n"
    )

    st.success(
        f"**Validation** \n\n"
        f"* The average images in the Cherry Leaves Visuliser page and \n"
        f"the image monatge show that the cherry leaves with a powdery \n"
        f"mildew have a distintive white marks resembling that of a \n"
        f"powder in comparison to the healthy cherry leaves which are \n"
        f"distinctively green."
    )

    st.write("### Business Requirement 2: Hypothesis and Validation")

    st.info(
        f"**Hypothesis** \n"
        f"* While it is fairly easy to look at one image of a cherry leaf \n"
        f"to see if it is healthy or has powdery mildew, examining \n"
        f"multiple images may not be so staright forward. We can \n"
        f"therefore facilitate the ability to upload images and for a \n"
        f"predition to be made as to whether the leaves are healthy or \n"
        f"have a powdery mildew on them by dragging and dropping the \n"
        f"images to a widget."
    )

    st.success(
        f"**Validation** \n\n"
        f"* When the images have been uploaded, each image clearly states \n"
        f"its prediction of whether it is a healthy cherry leaf image or \n"
        f"a cherry leaf image with a powdery mildew. A small graph also \n"
        f"indicates the probabilty. This is done with a 99% accuraccy \n"
        f"thus providing a sucessful outcome as the clients requirement \n"
        f"was 97%."
    )
