import api from './axios';

// GUVENLIK NOTU:
// JWT'yi localStorage'da saklamak XSS'e karsi savunmasizdir; bir XSS aciginda
// token calinabilir. Tercih edilen yontem, sunucunun token'i HttpOnly + Secure
// + SameSite cookie olarak set etmesidir (JS erisemez). Gecis yapilana kadar
// en azindan asagidaki onlemler alinmalidir:
//   - JWT'ye kisa omur (or. 15 dk) verin ve refresh token kullanin.
//   - Siki bir Content-Security-Policy (CSP) ile XSS yuzeyini daraltin.
//   - Cikista token'i mutlaka temizleyin.
// flask-jwt-extended varsayilan olarak "Authorization: Bearer <token>" basligini
// bekledigi icin token bu formatta gonderilir.

const setAuthToken = (token: string) => {
    if (token) {
        api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        localStorage.setItem('token', token);
    } else {
        delete api.defaults.headers.common['Authorization'];
        localStorage.removeItem('token');
    }
};

export default setAuthToken;
