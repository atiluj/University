function isPrime(x) {
    const sqrt = Math.sqrt(x);
    for (let i = 2; i <= sqrt; i++) {
      if (x % i === 0){
        return false;
      }
    }
    return true;
  }
  
  const result = [];
  for (let i = 2; i <= 100000; i++) {
    if (isPrime(i)) {
      result.push(i);
    }
  }
  
  console.info(result.join(" "));
  