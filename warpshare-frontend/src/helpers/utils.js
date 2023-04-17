import getRefreshToken from './tokens';


export const isTokenValid = (token) => {
    let isValid = false;

    token = localStorage.getItem('token');

    if (token) {
      isValid = fetch("http://127.0.0.1:8000/user/jwt/verify/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
        }),
      })
      .then((res) => {
        if (res.ok) {
          return true;
        }
        return false;
      })
      .catch((err) => {
        console.log(err);
      });
    }

    return isValid;
}

export const fetchShares = () => {
    return fetch("http://127.0.0.1:8000/share/list/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then((res) => {
        if (res.ok) {
            return res.json();
        }
        throw res;
    })
    .finally(() => {
        return shares;
    });
}

export const refreshTokens = () => {
    const tokens = window.localStorage.getItem("tokens");

  }