import axios from "axios";
import { TokenService } from "./storage/service";


export default axios.create({
  baseURL: "/api",
  headers: {
    Authorization: "Token " + TokenService.getToken()
  }
});