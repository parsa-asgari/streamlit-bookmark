## main.py
import streamlit as st

from streamlit_bookmark import streamlit_bookmark


def _submit_bookmark(bookmark_state, key):
    # prints the current Component's State

    # You could
    ## import requests
    ### And then invoke an external/internal API
    # print(key, bookmark_state)
    st.toast("Bookmarked key: %s %s"%(key, bookmark_state))
    return bookmark_state


def streamlit_bookmark_example(streamlit_bookmark, debug=False):

    st.title("💬 Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = [{'role': 'assistant', 'content': 'How can I help you?'}, {'role': 'user', 'content': 'g'}, {'role': 'assistant', 'content': 'dummy response'}, {'role': 'user', 'content': 'g'}, {'role': 'assistant', 'content': 'dummy response'}, {'role': 'user', 'content': 'g'}, {'role': 'assistant', 'content': 'dummy response'}]

        # Dummy statse for the bookmarks
        st.session_state['bookmark_1'] = {'bookmark': True}
        st.session_state['bookmark_2'] = {'bookmark': False}
        st.session_state['bookmark_3'] = {'bookmark': True}
        # Dummy-initial states for the bookmarks
        st.session_state['bookmark_1_last'] = True
        st.session_state['bookmark_2_last'] = False
        st.session_state['bookmark_3_last'] = True

    messages = st.session_state.messages

    # For each message in the chat, sets up the the relevant values in Streamlit's session_state
    ## This helps keeping the state of the components during a chat session
    for n, msg in enumerate(messages):
        st.chat_message(msg["role"]).write(msg["content"])
        if msg["role"] == "assistant" and n > 1:
            bookmark_key = f"bookmark_{int(n/2)}"

            if bookmark_key not in st.session_state:
                st.session_state[bookmark_key] = {"bookmark": False}

            # Ensures that the bookmark component's state does not "reset" when new responses are submitted by the user and the chat contunues
            component_state = (
                st.session_state[bookmark_key].get("bookmark")
                if st.session_state[bookmark_key]
                else None
            )

            # Here is the actual usage of the streamlit_bookmark component
            feedback = streamlit_bookmark(
                on_submit=_submit_bookmark,
                key=bookmark_key,
                component_state=component_state
            )

    # Executes only if the first text-input by the user is submitted.
    if prompt := st.chat_input(key=1):
        messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        if debug:
            response = "dummy response"
        else:
            response = "API CALL"

        with st.chat_message("assistant"):
            messages.append({"role": "assistant", "content": response})
            st.write(response)

        streamlit_bookmark(on_submit=_submit_bookmark, key=f"bookmark_{int(len(messages)/2)}", component_state=False)
    



# The main function's execution
streamlit_bookmark_example(streamlit_bookmark=streamlit_bookmark, debug=True)
