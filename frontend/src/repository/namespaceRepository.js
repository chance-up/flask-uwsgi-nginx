import { axios } from "@/axios/axios";

const URL_PREIFX = "/namespace";
export default class NamespaceRepository {
  async getAll() {
    try {
      const response = axios.get(URL_PREIFX + "/getAll");
      return Promise.resolve(response);
    } catch (error) {
      return Promise.reject(error);
    }
  }
}
