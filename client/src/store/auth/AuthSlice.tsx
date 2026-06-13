import axios from 'src/utils/axios';
import { createSlice } from '@reduxjs/toolkit';
import { AppDispatch } from 'src/store/Store';
import setAuthToken from 'src/utils/setAuthToken';

const initialState = {
    isAuthenticated: localStorage.getItem('token') ? true : false,
};

export const AuthSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        signin: (state, action) => {
            if (action.payload.access_token) {
                state.isAuthenticated = true;

                // Token'i sakla ve axios Authorization basligini ayarla
                // (korumali uclar @jwt_required ile artik bunu bekliyor).
                setAuthToken(action.payload.access_token);
            }
        },
        signup: (state, action) => {
            console.log("signup: ", action.payload)
        },
        signout: (state) => {
            state.isAuthenticated = false;

            // Token'i ve Authorization basligini temizle.
            setAuthToken('');
        }
    },
});

export const { signin, signup, signout } = AuthSlice.actions;

export const fetchSignIn = (payload: any) => async (dispatch: AppDispatch) => {
    try {
        const response = await axios.post('http://localhost:5000/login', payload);

        dispatch(signin(response.data));
    } catch (err) {
        throw new Error();
    }
};

export const fetchSignUp = (payload: any) => async (dispatch: AppDispatch) => {
    try {
        const response = await axios.post('http://localhost:5000/register', payload);

        dispatch(signup(response.data));
    } catch (err) {
        throw new Error();
    }
};

export default AuthSlice.reducer;
