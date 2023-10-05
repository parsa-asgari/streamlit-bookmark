import React, { useState, useEffect } from "react";
import Stack from '@mui/material/Stack';
import { Box } from "@mui/material";
import BookmarkIcon from '@mui/icons-material/Bookmark';
import BookmarkBorderIcon from '@mui/icons-material/BookmarkBorder';

export function BookmarkingWithToggle(props) {
    const [bookmarkSubmitted, setBookmarkSubmitted] = useState(false)

    useEffect(() => {
        if (props.disable_component){
            setBookmarkSubmitted(true);
        }
    }, [props.disable_component])

    const BookmarkHoverColor = () => {
            return "#f44336"
    }
    const handleBookmarkSubmission = () => {
        if (bookmarkSubmitted === false) {
            setBookmarkSubmitted(true);
            props.submitBookmark(true);
        } else {
            setBookmarkSubmitted(false);
            props.submitBookmark(false);
        }
    };

    return (
        <Box paddingY={0.5}>
            <Stack direction="row" spacing={1} justifyContent={props.align}>
                {bookmarkSubmitted ?  <BookmarkIcon
                    sx={{
                        fontSize: 28,
                        '&:hover': {
                            cursor: bookmarkSubmitted ? null : "pointer",
                            color: BookmarkHoverColor(),
                        }, }}
                    style={{ color:"red"}}
                    onClick={() => handleBookmarkSubmission()} /> 
                    : 
                    <BookmarkBorderIcon sx={{
                        fontSize: 28,
                        '&:hover': {
                            cursor: bookmarkSubmitted ? null : "pointer",
                            color: BookmarkHoverColor(),
                        }, }}
                    onClick={() => handleBookmarkSubmission()} />
                }
            </Stack>
        </Box>
        )
    }
