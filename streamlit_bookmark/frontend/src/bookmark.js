import React from "react";
import { BookmarkingWithToggle } from "./BookmarkingWithToggle";
import { Streamlit } from "streamlit-component-lib"

export function Bookmark(props) {
    const submitBookmark = (bookmark) => {
        Streamlit.setComponentValue({bookmark});
    };

    return (<BookmarkingWithToggle submitBookmark={submitBookmark} component_state={props.component_state} align={"flex-end"}/>)

}
