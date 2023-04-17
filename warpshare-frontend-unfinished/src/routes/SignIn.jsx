import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import { Link as LinkRouter, redirect } from "react-router-dom";
import { Navigate } from "react-router-dom";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { isTokenValid } from "../helpers/utils";
import { Alert } from "@mui/material";
const theme = createTheme();

export default function SignIn() {
  const [apiErrors, setApiErrors] = React.useState(null);

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);

    fetch("http://127.0.0.1:8000/user/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: data.get("email"),
        password: data.get("password"),
      }),
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        }
        throw res;
      })
      .then((res) => {
        window.localStorage.setItem("user", data.email);
        window.localStorage.setItem("token", res.token);
      })
      .catch((res) => {
        res.json().then((res) => {
          setApiErrors(res);
        });
      });
  };

  if (isTokenValid()) {
    return <Navigate replace to="/" />;
  } else {
    return (
      <ThemeProvider theme={theme}>
        <Container component="main" maxWidth="xs">
          <CssBaseline />
          <Box
            sx={{
              marginTop: 8,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign in
            </Typography>
            {
              apiErrors && (
                <Alert severity="error">
                  {
                    Object.keys(apiErrors).map((key, index) => (
                      <div key={index}>
                        {apiErrors[key]}
                      </div>
                    ))
                  }
                </Alert>
              )
            }
            <Box
              component="form"
              onSubmit={handleSubmit}
              noValidate
              sx={{ mt: 1 }}
            >
              <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                autoFocus
              />
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
              />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Sign In
              </Button>
              <Grid container justifyContent="flex-end">
                <Grid item>
                  <LinkRouter to="/sign-up/">
                    {"Don't have an account? Sign Up"}
                  </LinkRouter>
                </Grid>
              </Grid>
            </Box>
          </Box>
        </Container>
      </ThemeProvider>
    );
  }
}
