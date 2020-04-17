import http from "../http-common";

class DataService {
  getAllCustomers(strFilter) {
    return http.get(`/customers/?aktiv=true&${strFilter}`);
  }
  getCustomerObjects(id, strFilter) {
    return http.get(`/customers/${id}/objects/?${strFilter}`);
  }
  getAllMonths() {
    return http.get("/months/");
  }
  getMonth(id) {
    return http.get(`/months/${id}/`);
  }
  updateMonth(id, data) {
    return http.put(`/months/${id}/`, data);
  }
  getPrevCustomers() {
    return http.get("/prev_customers/");
  }
  getEtgs(id, strFilter) {
    return http.get(`/customers/${id}/etgs/?${strFilter}`);
  }
  getLokasjons(id, strFilter) {
    return http.get(`/customers/${id}/lokasjons/?${strFilter}`);
  }
  getPlasserings(id, strFilter) {
    return http.get(`/customers/${id}/plasserings/?${strFilter}`);
  }
  getCustomer(id) {
    return http.get(`/customers/${id}/`);
  }
  getObject(id) {
    return http.get(`/objects/${id}/`);
  }
  updateObject(id, data) {
    return http.patch(`/objects/${id}/`, data);
  }
  getAllExtinguishants() {
    return http.get("/extinguishants/");
  }
}

export default new DataService();
