// 1. Basic Authentication Middleware
const basicAuth = (req, res, next) => {
    const secretToken = "my-secure-token-123"; // In a real app, use process.env.TOKEN
    const userToken = req.headers['authorization'];

    if (userToken === secretToken) {
        next(); // Authorized
    } else {
        res.status(401).send("Unauthorized: Invalid Token");
    }
};

// 2. Input Validation (Example for a Login or Search route)
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Validation Place 1: Check if fields are empty
    if (!username || !password) {
        return res.status(400).send("Error: Username and Password are required.");
    }

    // Validation Place 2: Check length/format
    if (username.length < 3 || username.length > 20) {
        return res.status(400).send("Error: Username must be between 3-20 characters.");
    }

    res.send("Login successful!");
});