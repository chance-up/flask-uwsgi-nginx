import { axios } from "@/axios/axios";

const URL_PREIFX = "/connection";
export default class NamespaceRepository {
  async connect() {
    try {
      const response = axios.get(URL_PREIFX + "/connect");
      return Promise.resolve(response);
    } catch (error) {
      return Promise.reject(error);
    }
  }

  async dfh() {
    try {
      const response = axios.get(URL_PREIFX + "/dfh");
      return Promise.resolve(response);
    } catch (error) {
      return Promise.reject(error);
    }
  }
  async disConnect() {
    try {
      const response = axios.get(URL_PREIFX + "/disconnect");
      return Promise.resolve(response);
    } catch (error) {
      return Promise.reject(error);
    }
  }
}
