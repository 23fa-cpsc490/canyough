function isItSortedNow(arr: any) {
  for (let i: any = 1; i < arr.length; i++) {
    if (arr[i - 1] > arr[i]) {
      return false;
    }
  }
  return true;
}
function tryingToSortNow(arr: any) {
  for (let i: any = arr.length - 1; i > 0; i--) {
    const j: any = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}

// Bogosort algorithm
const bogosort = (arr: any) => {
  while (!isItSortedNow(arr)) {
    tryingToSortNow(arr);
  }
  return arr;
};