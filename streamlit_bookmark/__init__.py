import os

import streamlit as st
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_bookmark", url="http://localhost:3001"
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_bookmark", path=build_dir)


def streamlit_bookmark(
    on_submit,
    component_state,
    key=None,
):
    """Creates a new instance of "streamlit_bookmark". Receives the current bookmark status for a given Streamlit compnent and calls a function upon submission.

    Parameters
    ----------
    on_submit: callable
        A callback invoked when feedback is submitted. This function must accept at least one argument, the feedback response dict,
        allowing you to save the feedback to a database for example. Additional arguments can be specified using `args` and `kwargs`.
    component_state: boolean
        A boolean to set the state of the bookmark.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict
        The bookmark state

    """

    # Initiate dict-keys or variables in case they are not defined
    if key is None:
        key = "bookmark_1"
    if f"{key}_last" not in st.session_state:
        st.session_state[f"{key}_last"] = False
    if f"{key}" not in st.session_state:
        st.session_state[f"{key}"] = {"bookmark": False}

    # Invokes the react frontend's side
    component_value = _component_func(
        key=key,
        component_state=component_state,
        default=None,
    )

    # Checks to see if the bookmark's state has changed or not.
    # If so, invoke the on_submit function
    ## Current State != Previous State
    if component_value["bookmark"] != st.session_state[f"{key}_last"]:
        on_submit(bookmark_state=component_value["bookmark"], key=f"{key}_last")

    # Updates the current bookmarking status for the {key} component
    st.session_state[f"{key}_last"] = component_value["bookmark"]

    return component_value
