"""
Unit tests for the `show` method of class D in diamond_problem.py.

Tested method:
    diamond_problem.D.show

Test categories:
    - Happy paths: Normal, expected usage.
    - Edge cases: Unusual or boundary conditions.

All tests are organized in TestDShow.
"""

import pytest
from diamond_problem import A, B, C, D

class TestDShow:
    @pytest.fixture
    def d_instance(self):
        """Fixture to provide a fresh instance of D for each test."""
        return D()

    # ------------------- Happy Path Tests -------------------

    @pytest.mark.happy_path
    def test_show_on_d_prints_class_d(self, capsys, d_instance):
        """
        Happy path: Ensure D.show() prints 'Class D'.
        """
        d_instance.show()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Class D"

    @pytest.mark.happy_path
    def test_show_on_b_prints_class_b(self, capsys):
        """
        Happy path: Ensure B.show() prints 'Class B'.
        """
        b = B()
        b.show()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Class B"

    @pytest.mark.happy_path
    def test_show_on_c_prints_class_c(self, capsys):
        """
        Happy path: Ensure C.show() prints 'Class C'.
        """
        c = C()
        c.show()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Class C"

    @pytest.mark.happy_path
    def test_show_on_a_prints_class_a(self, capsys):
        """
        Happy path: Ensure A.show() prints 'Class A'.
        """
        a = A()
        a.show()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Class A"

    @pytest.mark.happy_path
    def test_d_inherits_show_from_d_not_b_or_c(self, capsys, d_instance):
        """
        Happy path: Ensure D.show() does NOT print 'Class B' or 'Class C'.
        """
        d_instance.show()
        captured = capsys.readouterr()
        assert captured.out.strip() != "Class B"
        assert captured.out.strip() != "Class C"

    # ------------------- Edge Case Tests -------------------

    @pytest.mark.edge_case
    def test_show_on_d_with_args_raises_typeerror(self, d_instance):
        """
        Edge case: Calling D.show() with unexpected arguments should raise TypeError.
        """
        with pytest.raises(TypeError):
            d_instance.show("unexpected_argument")

    @pytest.mark.edge_case
    def test_show_on_d_with_kwargs_raises_typeerror(self, d_instance):
        """
        Edge case: Calling D.show() with unexpected keyword arguments should raise TypeError.
        """
        with pytest.raises(TypeError):
            d_instance.show(foo="bar")

    @pytest.mark.edge_case
    def test_show_on_d_multiple_calls_consistent_output(self, capsys, d_instance):
        """
        Edge case: Multiple calls to D.show() should consistently print 'Class D'.
        """
        for _ in range(3):
            d_instance.show()
            captured = capsys.readouterr()
            assert captured.out.strip() == "Class D"

    @pytest.mark.edge_case
    def test_show_on_d_after_reassignment_of_show(self, capsys, d_instance):
        """
        Edge case: If D.show is reassigned, ensure the new behavior is reflected.
        """
        def new_show(self):
            print("New Show")
        d_instance.show = new_show.__get__(d_instance, D)
        d_instance.show()
        captured = capsys.readouterr()
        assert captured.out.strip() == "New Show"

    @pytest.mark.edge_case
    def test_show_on_d_via_super_calls_parent_show(self, capsys, d_instance):
        """
        Edge case: Directly calling super().show() from D should print 'Class B'.
        """
        # Dynamically add a method to call super().show()
        def call_super_show(self):
            super(D, self).show()
        d_instance.call_super_show = call_super_show.__get__(d_instance, D)
        d_instance.call_super_show()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Class B"