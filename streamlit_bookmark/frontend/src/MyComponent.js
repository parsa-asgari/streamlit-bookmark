import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React from "react"
import { Bookmark } from "./bookmark"


class MyComponent extends StreamlitComponentBase {

  render() {
    return (
      <div>
        <Bookmark
          component_state={this.props.args["component_state"]}
          default={this.props.args["default"]}
        />
      </div>
    )
  }
}

export default withStreamlitConnection(MyComponent)
