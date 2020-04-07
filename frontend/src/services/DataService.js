import http from "../http-common";

class DataService {
  getAllCustomers() {
    return http.get("/customers/");
  }
  getAllObjects() {
      return http.get("/objects/");
  }
  getAllMonths() {
    return http.get("/months/")
  }
  getPrevCustomers() {
    return http.get("/prev_customers/");
  }
  getEtgs(id) {
    return http.get(`/customers/${id}/etgs/`);
  }
  getLokasjons(id) {
    return http.get(`/customers/${id}/lokasjons/`);
  }
  getPlasserings(id) {
    return http.get(`/customers/${id}/plasserings/`);
  }
  getCustomer(id) {
    return http.get(`/customers/${id}/`);
  }
  getObject(id) {
    return http.get(`/objects/${id}/`);
  }
}

export default new DataService();