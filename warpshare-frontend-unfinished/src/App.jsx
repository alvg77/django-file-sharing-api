import { Route, Routes } from 'react-router-dom'
import SignIn from './routes/SignIn'
import SignUp from './routes/SignUp'
import ErrorPage from './error-page'
import Navbar from './Navbar'
import Upload from './routes/Upload'
import History from './routes/History'
import Shares from './routes/Shares'

export default function App() {
    return (
        <>
            <Navbar />
            <div style={{
                paddingTop: '64px',
                width: '100%',
            }}>
                <Routes>
                    <Route path="/" element={<Shares />} errorElement={<ErrorPage />} />
                    <Route path="/sign-in" element={<SignIn />} errorElement={<ErrorPage />} />
                    <Route path="/sign-up" element={<SignUp />} errorElement={<ErrorPage />} />
                    <Route path="/history" element={<History />} errorElement={<ErrorPage />} />
                    <Route path="/shares" element={<Shares />} errorElement={<ErrorPage />} />
                    <Route path="/upload" element={<Upload />} errorElement={<ErrorPage />} />

                </Routes>
            </div>
        </>
    );
}