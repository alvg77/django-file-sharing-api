import { isTokenValid } from "../helpers/utils";
import React from "react";
import { Navigate } from "react-router-dom";
import { fetchShares } from "../helpers/utils";
import Container from "@mui/material/Container";

export default function Root() {
    const [sharedFiles, setSharedFiles] = React.useState([]);

    if (!isTokenValid()) {
        return <Navigate replace to="/sign-in" />;
    } else {
        // setSharedFiles(fetchShares)
        // return (
        //     <Container>
        //     { sharedFiles.map((file) => {
        //             return (
        //                 <div>
        //                     <h1>{file.name}</h1>
        //                     <p>{file.description}</p>
        //                 </div>
        //             );
        //         })
        //     }
        //     </Container>
            
        // );
    }
}