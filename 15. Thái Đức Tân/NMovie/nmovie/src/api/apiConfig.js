const apiConfig = {
  baseUrl: "https://api.themoviedb.org/3/",
  apiKey: "303d6456e0f0fa4e02767537f864f138",
  originalImage: (imgPath) => `https://image.tmdb.org/t/p/original/${imgPath}`,
  w500Image: (imgPath) => `https://image.tmdb.org/t/p/w500/${imgPath}`,
};

export default apiConfig;
