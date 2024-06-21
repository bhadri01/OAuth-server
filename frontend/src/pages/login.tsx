import { useState } from 'react';
import axios from 'axios';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (e: any) => {
        e.preventDefault();
        try {
            const response = await axios.post('/auth/login', {
                username,
                password,
            });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="flex flex-col items-center justify-center p-6 bg-white shadow-md rounded-md">
            <h2 className="text-2xl font-bold mb-6">Log In</h2>
            <form onSubmit={handleLogin} className="w-full max-w-md">
                <div className="mb-4">
                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-600"
                    />
                </div>
                <div className="mb-6">
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-600"
                    />
                </div>
                <button
                    type="submit"
                    className="w-full bg-indigo-600 text-white py-2 rounded-md hover:bg-indigo-700 transition duration-300"
                >
                    Log In
                </button>
            </form>
        </div>
    );
}

export default Login;
