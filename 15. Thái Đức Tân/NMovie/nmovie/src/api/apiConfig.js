const apiConfig = {
  baseUrl: "https://www.themoviedb.org/3/",
  apiKey: "15e383204c1b8a09dbfaaa4c01ed7e17",
  originalImange: (imgPath) => `https://image.tmdb.org/t/p/original/${imgPath}`,
  w500Imange: (imgPath) => `https://image.tmdb.org/t/p/w500/${imgPath}`,
};

export default apiConfig;
