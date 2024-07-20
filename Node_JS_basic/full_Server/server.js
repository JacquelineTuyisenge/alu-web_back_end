/* eslint-disable */
import express from 'express';
import controllerRouting from './routers/index';

const app = express();
const port = 1245;

controllerRouting(app);

app.listen(port, () => {
});

export default app;
