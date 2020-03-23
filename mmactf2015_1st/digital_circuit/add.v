module mux(f, a, b, sel);
  output f;
  input a, b, sel;
  assign f = sel ? a : b;
endmodule

module main;
  reg a, b, c;
  initial begin
    a = 0;
    b = 0;
    c = 0;
    sel = 0;
  end
  initial
    mux (o, a, b, sel);
    $display("Output = %s", o);
  $finish;
endmodule
