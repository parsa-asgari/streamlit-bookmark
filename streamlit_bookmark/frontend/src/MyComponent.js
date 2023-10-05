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
          disable_component={this.props.args["disable_component"]}
          default={this.props.args["default"]}
        />
      </div>
    )
  }
}

export default withStreamlitConnection(MyComponent)
