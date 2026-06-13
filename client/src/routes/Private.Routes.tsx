import { Navigate, Outlet } from "react-router";
import { useSelector } from "src/store/Store";

// GUVENLIK NOTU:
// Bu bilesen yalnizca bir kullanici deneyimi (UX) korumasidir; client tarafinda
// kolayca atlatilabilir. Asil yetkilendirme SUNUCUDA yapilmalidir: tum korumali
// API uclari flask-jwt-extended'in @jwt_required() dekoratoru ile korunmaktadir
// (bkz. server/routes.py). Bu nedenle gecersiz/eksik token ile yapilan istekler
// sunucu tarafinda 401 ile reddedilir.

const PrivateRoute = () => {
    const isAuthenticated = useSelector(state => state.authReducer.isAuthenticated);

    if (isAuthenticated) {
        return <Outlet />;
    } else {
        return <Navigate to="/auth/sign-in" />;
    }
}

export default PrivateRoute;
