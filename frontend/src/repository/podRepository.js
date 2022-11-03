import { axios } from "@/axios/axios";

export default class PodRepository {
  async getAllPod() {
    try {
      const response = axios.get("/a").then((res) => {
        console.log(res.data);
      });
      return Promise.resolve(response);
    } catch (error) {
      return Promise.reject(error);
    }
  }
}
