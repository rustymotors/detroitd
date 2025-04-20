import { fileURLToPath } from "node:url";
import { dirname } from "node:path";
import express from "express";
import RateLimit from "express-rate-limit";

const app = express();
const router = express.Router();

// set up rate limiter: maximum of five requests per minute
var limiter = RateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // max 100 requests per windowMs
});

// apply rate limiter to all requests
app.use(limiter);

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const path = __dirname + "/views/";
const port = 8080;

router.use(function (req, res, next) {
  console.log(req.method + " " + req.url);
  next();
});

router.get("/", function (req, res) {
  res.sendFile(path + "index.html");
});

router.get("/healthchk", function (req, res) {
  res.send("OK");
});

app.use("/", router);

app.listen(port, function () {
  console.log("Server is running on port " + port);
});
