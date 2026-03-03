import sys
import os

from google import genai
from google.genai import types

from dotenv import load_dotenv

from call_function import available_functions,call_function
from prompts import system_prompt


def main():
	load_dotenv()

	verbose = "--verbose" in sys.argv  # returns a boolean (True/False)
	args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

	if not args:
		print("AI Code Assistant")
		print('\nUsage: python main.py "your prompt here" [--verbose]')
		print('Example: python main.py "How do I build a calculator app?"')
		sys.exit(1)
	user_prompt = " ".join(args)

	messages = [
			types.Content(role="user", parts=[types.Part(text=user_prompt)]),
			]

	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)

	if verbose:
		print(f"User prompt: {user_prompt}\n")

	generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
	for _ in range(20):
		response = client.models.generate_content(
				# model="gemini-2.0-flash-001",
				#model="gemini-2.0-flash",
				model="gemini-2.5-flash",
				# model="gemini-2.5-flash-lite",
				# model="gemini-3-flash-preview",
				#model="gemini-3-pro-preview",
				#model="gemini-3.1-pro-preview",
				contents=messages,
				config=types.GenerateContentConfig(
					tools=[available_functions], system_instruction=system_prompt
					),
				)
		if response.candidates:
			for candidate in response.candidates:
				messages.append(candidate.content)

		if verbose:
			print("Prompt tokens:", response.usage_metadata.prompt_token_count)
			print("Response tokens:", response.usage_metadata.candidates_token_count)

		if not response.function_calls:
			print("Response:")
			print(response.text)
			return

		function_responses = []

		for function_call in response.function_calls:
			result = call_function(function_call, verbose)
			if (
				not result.parts
				or not result.parts[0].function_response
				or not result.parts[0].function_response.response
			):
				raise RuntimeError(f"Empty function response for {function_call.name}")
			if verbose:
				print(f"-> {result.parts[0].function_response.response}")
			function_responses.append(result.parts[0])
			#print(f"Calling function: {function_call.name}({function_call.args})")

		messages.append(types.Content(role="user", parts=function_responses))

	print('Out of bounds: maximum number of iterations reached')
	sys.exit(1)


if __name__ == "__main__":
	main()
