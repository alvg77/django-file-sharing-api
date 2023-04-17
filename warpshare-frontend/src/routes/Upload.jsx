import React, { useRef, useState } from 'react';
import AWS from 'aws-sdk';
import { TextField } from '@mui/material';

const Upload = () => {
  const fileInputRef = useRef(null);
  const emailRef = useRef(null);
  const [errors, setErrors] = useState([]);

  const share = async () => {
    const filename = fileInputRef.current.files[0].name;
    const email = emailRef.current.value;

    let response = fetch ('http://localhost:8000/share/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                filename: filename,
                email: email,
                }),
            })
            .then(res => {
                if (res.ok) {
                    return res.json();
                }
                throw res;
            })
        //     .catch(res => {
        //         res.json().then(res => {
        //             setErrors(res);
        //         });
        //         return null;
        //     }
        // );
    console.log(response);
    
    return response;
  }

  const handleFileUpload = async () => {
    const file = fileInputRef.current.files[0];

    if (!file) {
      alert('No file selected');
      return;
    }

    if (!emailRef.current.value) {
        alert('No email to share provided');
        return;
    }
    share()
    // if (!share()) {
    //     alert('No user with such email');
    //     return;
    // }
    

    const spacesEndpoint = new AWS.Endpoint(import.meta.env.VITE_DO_SPACES_URL);
    const s3Client = new AWS.S3({
      endpoint: spacesEndpoint,
      accessKeyId: import.meta.env.VITE_DO_SPACES_KEY,
      secretAccessKey: import.meta.env.VITE_DO_SPACES_SECRET,
    });

    const uploadParams = {
      Bucket: import.meta.env.VITE_DO_SPACES_BUCKET,
      Key: `uploads/${file.name}`,
      Body: file,
    };

    try {
      await s3Client.upload(uploadParams).promise();
      console.log('File uploaded successfully!');
    } catch (error) {
      console.error(error);
      alert('Something went wrong');
    }
  };

  return (
    <div>
      <input type="file" ref={fileInputRef} />
      <input type="text" ref={emailRef} />
      <button onClick={handleFileUpload}>Upload File</button>
    </div>
  );
};

export default Upload;