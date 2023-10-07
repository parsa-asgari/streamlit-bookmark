# streamlit-bookmark

Here is a Streamlit component that allows you to **bookmark chat messages** in your apps, for later reference or anything else.
The code is based on [streamlit-feedback by Trubrics](https://github.com/trubrics/streamlit-feedback)

## Install

```sh
pip install streamlit-bookmark
```

## Examples

- See the streamlit_app_example.py.

## Usage

This component holds a single function:

```python
from streamlit_bookmark import streamlit_bookmark
bookmark_state = streamlit_bookmark(on_submit=some_callback_function,
                key=SOME_COMPONENT_KEY,
                disable_component=True)
bookmark_state
# ===> {'bookmark': True}
```


Could be used with these parameters:

```python
def streamlit_bookmark(
    on_submit=None,
    disable_component=None,
    key=None,
):
    """Creates a new instance of "streamlit_bookmark". Receives the current bookmark status for a given Streamlit compnent and calls a function upon submission.

    Parameters
    ----------
    on_submit: callable
        An optional callback invoked when feedback is submitted. This function must accept at least one argument, the feedback response dict,
        allowing you to save the feedback to a database for example. Additional arguments can be specified using `args` and `kwargs`.
    disable_component: str
        An optional boolean to disable the component. Can be used to pass state from one component to another.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict
        The user response

    """
```
For the code example, see [here](streamlit_app_example.py).
