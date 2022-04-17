void vuln(void)
{
  char local_3e [54];
  
  __x86.get_pc_thunk.ax();
  gets(local_3e);
  return;
}

void win(int param_1)
{
  int iVar1;
  
  iVar1 = __x86.get_pc_thunk.ax();
  if (param_1 == -0x21524111) {
    system((char *)(iVar1 + 0x12e));
  }
  return;
}
