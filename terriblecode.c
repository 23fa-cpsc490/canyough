unsigned int add(unsigned int m, unsigned int n){
  goto c;
  a:
    int i = 0;
  b:
    if (n = 0) return m;
    m = succ(m);
    goto d;
  c:
    goto a;
  d:
    i++;
    n--;
    goto b;
}
