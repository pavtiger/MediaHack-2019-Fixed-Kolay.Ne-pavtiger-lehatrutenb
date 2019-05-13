#ifdef python
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
namespace py = pybind11;
#else
#include <stdexcept>
#endif

#include <vector>
#include <string>


namespace VericStrong
{
	std::string dumps(const std::vector<std::string> &obj)
	{
		std::string ans = "";
		for(const std::string &s : obj)
		{
			ans += '"';
			for(const char &c : s)
			{
				if((c != '\\') && (c != '"'))
					ans += c;
				else
				{
					ans += '\\';
					ans += c;
				}
			}
		}
		return ans;
	}

	std::vector<std::string> loads(const std::string &dump)
	{
		std::vector<std::string> ans;
		try
		{
			bool backslash = 0;
			for(const char &c : dump)
			{
				if(backslash)
				{
					ans.back() += c;
					backslash = 0;
					continue;
				}
				switch(c)
				{
				case '"':
					ans.push_back("");
					break;
				case '\\':
					backslash = true;
					break;
				default:
					ans.at(ans.size() - 1) += c;
				}
			}
		}
		catch(...)
		{
			throw std::invalid_argument("The given argument is not a VericStrong string");
		}
		return ans;
	}
}

#ifdef python
PYBIND11_MODULE(vericstrong, m)
{
	m.doc() = "VericStrong module for dumping vectors of strings into strings and back";
	m.def("dumps", &VericStrong::dumps, "A function for dumping a vector of strings");
	m.def("loads", &VericStrong::loads, "A function for back loagins the vector of strings from a string");
}
#endif
