import axios from "axios";
import { TokenService } from "./storage/service";


export default axios.create({
  baseURL: "http://localhost:8000/api",
  headers: {
    Authorization: "Token " + TokenService.getToken()
  }
});