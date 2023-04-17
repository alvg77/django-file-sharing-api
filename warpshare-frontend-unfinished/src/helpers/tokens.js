function saveAccessToken (accessToken) {
    localStorage.setItem('accessToken', accessToken);
}

function getAccessToken () {
    return localStorage.getItem('accessToken');
}

function saveRefreshToken (refreshToken) {
    localStorage.setItem('refreshToken', refreshToken);
}

function getRefreshToken () {
    return localStorage.getItem('refreshToken');
}

function removeTokens () {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
}

export default {
    saveAccessToken,
    getAccessToken,
    saveRefreshToken,
    getRefreshToken,
    removeTokens,
};